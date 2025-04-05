import { Router } from "express";
import { signOut, signin, signup } from "../controllers/authController";

const router = Router();

router.post("/signup", signup);
router.post("/signin", signin);
router.get("/signout", signOut);

export default router;
