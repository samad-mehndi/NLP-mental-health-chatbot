import User, { findOne } from "../models/user";
import { hashSync, compareSync } from "bcryptjs";
import { sign } from "jsonwebtoken";

export const signup = async (req, res, next) => {
    const { username, email, password } = req.body;
    const hashedPassword = hashSync(password, 10);
    const newUser = new User({ username, email, password: hashedPassword });
    try {
      await newUser.save();
      res.status(201).json('User created successfully!');
    } catch (error) {
      next(error);
    }
};
  
export const signin = async (req, res, next) => {
    const { email, password } = req.body;
    try {
      const validUser = await findOne({ email });
      if (!validUser) return res.status(404).json({ error: "User not found" });
      const validPassword = compareSync(password, validUser.password);
        if (!validPassword) return res.status(401).json({ error: 'Wrong credentials!' });
      const token = sign({ id: validUser._id }, process.env.JWT_SECRET);
      const { password: pass, ...rest } = validUser._doc;
      res
        .cookie('access_token', token, { httpOnly: true })
        .status(200)
        .json(rest);
    } catch (error) {
      next(error);
    }
};
  
export const signOut = async (req, res, next) => {
    try {
      res.clearCookie('access_token');
      res.status(200).json('User has been logged out!');
    } catch (error) {
      next(error);
    }
};
