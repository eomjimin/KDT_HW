import { get } from "mongoose";
import Mongoose from "mongoose";


const db_host = "mongodb+srv://jimini0920:JW4qxzzylk41IZe1@cluster0.kngcohp.mongodb.net/?retryWrites=true&w=majority"

let db;

export async function connectDB(){
    try{
        const connection = await Mongoose.connect(db_host, {
            dbName: 'banapresso'
        });
        db = connection.connection;
    }
    catch(error){
        console.error('연결실패!')
        throw error;
    }
    // console.log('db연결!')
    // return Mongoose.connect(db_host);
}

export function getInfo(){
    return db.collection("stores");
}

export async function getAll() {
    try{
        await connectDB();

        // const info = getInfo();

        const data = await getInfo().find().toArray();
        return data;
    }
    catch(error){
        console.log(error);
        throw error;
    }
    finally{
        Mongoose.connection.close();
    }
}

export async function getStoreInformation(req, res){
    try {
        const data = await getAll();
        res.status(200).json(data);
    } catch(error){
        console.error('서버 연결 실패!');
        res.status(500).json({error: '서버 연결 실패!'});
    }
}