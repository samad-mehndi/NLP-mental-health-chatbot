# CS 6320.001 - Natural Language Processing - S25  
## University of Texas at Dallas (UTD) - Department of Computer Science  
**Instructor:** Dr. Tatiana  

## Project Title: Mental Health Support Chatbot  

**YouTube Demo:** https://www.youtube.com/watch?v=bWrb6nlwzFs  

### Team Members:
- **Nikita Kachane**  
- **Samad Mehndi** (NetID: sxm230312)  
- **Nikita Ramachandran** (NetID: nxr200026)  

---

## Objective  
The goal of this project is to develop a mental health chatbot capable of understanding user queries and responding with empathetic, relevant answers. The chatbot uses Natural Language Processing (NLP) techniques including intent classification and semantic similarity matching. It is built using FastAPI for the backend and incorporates HuggingFace Transformer models and Sentence-BERT for natural language understanding. A React-based frontend allows users to interact with the chatbot via a web interface.

---

## Approach  
Our system combines two NLP strategies: intent classification and semantic search.  
- When a user sends a message, the chatbot first predicts the intent using a Transformer-based classifier.  
- If the intent does not yield a confident response, the chatbot falls back on semantic similarity matching against a dataset of mental health FAQs.

### Technical Details:
- **Intent Classification:** Fine-tuned HuggingFace transformer model.
- **Semantic Matching:** Sentence-BERT (all-MiniLM-L6-v2) computes embeddings; cosine similarity is used to match questions.
- **Backend:** FastAPI with a `/chat` REST endpoint.
- **Frontend:** React application for real-time chatbot interaction.

---

## Enhancements Over Base Models
- **Offline Model Loading:** Supports fast startup with pre-downloaded models.
- **Custom Intent Classifier:** Trained for common mental health intents.
- **Precomputed Semantic Embeddings:** Enables fast runtime search.
- **Fallback Matching Logic:** Uses cosine similarity when classification confidence is low.
- **Modular Design:** Clean separation of concerns.
- **React Frontend Integration:** Provides a modern interface for interaction.

---

## Lessons Learned
- Clean, structured data improves performance and relevance.
- Model quality (e.g., all-MiniLM-L6-v2) significantly impacts semantic accuracy.
- FastAPI is lightweight and ML-friendly.
- Frontend-backend integration requires careful testing (e.g., CORS, data formats).
- Offline deployment requires managing caches and model paths.
- Consistent team collaboration is critical for success.

---

## Contributions

### Nikita Kachane
- Researched and selected Sentence-BERT.
- Implemented semantic similarity logic.
- Preprocessed mental health FAQ data.
- Managed embedding generation and serialization.

### Samad Mehndi
- Developed FastAPI backend.
- Integrated React frontend with backend.
- Handled environment setup and Uvicorn deployment.
- Managed GitHub repo and full-stack testing.

### Nikita Ramachandran
- Developed and fine-tuned intent classifier.
- Handled model loading, caching, and offline support.
- Serialized embeddings and labels with Pickle.
- Wrote much of the documentation and final report.

---

## Self-Scoring

### Nikita Kachane – 150/160
- **80 pts:** Explored embedding models and semantic logic.  
- **30 pts:** Dual strategy with intent + semantic search.  
- **10 pts:** Data preprocessing and embedding management.  
- **10 pts:** Shared insights on embedding quality and caching.  
- **10 pts:** GitHub repo and documentation contributions.  
- **10 pts:** External testing of chatbot performance.  
- **10 pts:** Earned money – N/A.  
- **Deductions:** None.

### Samad Mehndi – 150/160
- **80 pts:** Built backend and frontend integration.  
- **30 pts:** REST-React bridge with usable interface.  
- **10 pts:** Managed dependencies, state, CORS.  
- **10 pts:** Reflected on modular design and integration.  
- **10 pts:** Led repo cleanup and ReadMe clarity.  
- **10 pts:** External usability testing.  
- **10 pts:** Earned money – N/A.  
- **Deductions:** None.

### Nikita Ramachandran – 150/160
- **80 pts:** Intent classifier development and tuning.  
- **30 pts:** Offline loading with caching optimization.  
- **10 pts:** Coordinated models and integration logic.  
- **10 pts:** Authored reflection sections of report.  
- **10 pts:** Repo and documentation.  
- **10 pts:** External testing and feedback.  
- **10 pts:** Earned money – N/A.  
- **Deductions:** None.

---

## Conclusion  
This project demonstrates the effectiveness of combining intent classification and semantic search to build an empathetic, responsive mental health chatbot. It features a modular design, optimized inference, and a full-stack implementation with both backend (FastAPI) and frontend (React). The system can be further scaled and improved with session tracking, cloud deployment, and multilingual support.

---

## Future Improvements
- Add user session tracking and memory of past interactions.  
- Deploy to a cloud platform (e.g., AWS).  
- Expand React frontend with authentication, theming, and better UI.  
- Introduce crisis escalation with professional referrals.  
- Add multilingual support via translation APIs or multilingual models.  
