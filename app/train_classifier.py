import pandas as pd
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import torch
import joblib

# 1. Load and encode dataset
df = pd.read_csv("data.csv")
df = df.sample(n=2000, random_state=42) 
df.rename(columns={"questionText": "text"}, inplace=True)
label_encoder = LabelEncoder()

df["label_id"] = label_encoder.fit_transform(df["topic"])

# Save the label encoder
joblib.dump(label_encoder, "label_encoder.pkl")

# Convert to Hugging Face Dataset
dataset = Dataset.from_pandas(df[["text", "label_id"]])
dataset = dataset.train_test_split(test_size=0.2)

# 2. Tokenize
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def tokenize_and_align_labels(batch):
    tokens = tokenizer(batch["text"], padding=True, truncation=True)
    tokens["labels"] = batch["label_id"]
    return tokens

dataset = dataset.map(tokenize_and_align_labels, batched=True)

# 3. Load Model
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=len(label_encoder.classes_)
)

# 4. Metrics
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = torch.argmax(torch.tensor(logits), dim=1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='weighted')
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc, "precision": precision, "recall": recall, "f1": f1}

# 5. Training config
training_args = TrainingArguments(
    output_dir="./mental_health_classifier",
    learning_rate=2e-5,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_dir="./logs"
)


# 6. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

# 7. Train and save
trainer.train()
model.save_pretrained("mental_health_classifier")
tokenizer.save_pretrained("mental_health_classifier")