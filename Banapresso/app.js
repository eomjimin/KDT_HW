import Mongoose from 'mongoose'
import express from "express"
import cors from "cors";
import router from './router.js';
import { connectDB } from './database.js';

const app = express();
app.use(cors());
app.use(express.json());


app.use("/banapresso", router)

app.use((req, res, next) => {
    res.sendStatus(404);
})

connectDB().then(()=>
    app.listen(8080)
).catch(console.error)





