import express from "express";
import dotenv from 'dotenv'
import cors from 'cors'
import jwt from "jsonwebtoken";
import { initializeApp } from 'firebase/app';
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";
import { getAuth as getAuthAdmin } from 'firebase-admin/auth';
import { initializeApp as initializeAppaAdmin}  from 'firebase-admin/app';
import 'firebase/firestore';
import 'firebase/auth';

// const firebase = require("firebase/app");

const firebaseConfig = {
    apiKey: "AIzaSyB4sijiLPRCypRxiVxu022dCFC9VOemJqU",
    authDomain: "medht-d6f34.firebaseapp.com",
    projectId: "medht-d6f34",
    storageBucket: "medht-d6f34.appspot.com",
    messagingSenderId: "823429798580",
    appId: "1:823429798580:web:9b6890866ef46d48be15e1",
    measurementId: "G-60WDJL9Q1N"
  };
const fb = initializeApp(firebaseConfig);
const fbAdm = initializeAppaAdmin(firebaseConfig); //тут трабл

const auth = getAuth();
console.log("27 line", auth.getUser);


dotenv.config()

const PORT = process.env.PORT || 3001


const app = express();

app.use(express.json());
app.use(cors());


//Регистрация с токеном
app.post('/auth/registration', async (req, res)=>{
    try{
        
    }catch(err){
        res.json({message:"error on registration"})
    }
})

app.use(express.json())
app.listen(PORT,(err)=>{
    if(err){
        return console.log(err);
    }
    console.log("ok")
});