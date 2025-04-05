import express, { json } from 'express';
import { config } from 'dotenv';
import cors from 'cors';
import connectDB from './config/db';
import cookieParser from 'cookie-parser';
import authRouter from './routes/authRoutes.js';

config();
connectDB();

const app = express();
app.use(cors());
app.use(json());
app.use(cookieParser());

// Routes
app.use('/api/auth', authRouter);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));