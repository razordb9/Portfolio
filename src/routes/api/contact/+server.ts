import type { RequestHandler } from './$types';
import nodemailer from 'nodemailer';
import { SECRET_GMAIL_PWD, SECRET_GMAIL_ACC } from '$env/static/private';

export const POST: RequestHandler = async ({ request }) => {
  try {
    const { name, email, message } = await request.json();
    
    console.log({ name, email, message });

    const transporter = nodemailer.createTransport({
      host: "smtp.gmail.com",
      port: 587,
      secure: false, // true for port 465, false for other ports
      auth: {
        user: SECRET_GMAIL_ACC,
        pass: SECRET_GMAIL_PWD,
      },
    });

    await new Promise((resolve, reject) =>{
      transporter.verify(function (error, success){
        if (error) {
          console.log(error);
          reject(error);
        } else {
          console.log("Server is ready to take your message");
          resolve(success);
        }
      })
    })

    const mailData = {
      from: email, // sender address
      to: SECRET_GMAIL_ACC, // list of receivers
      subject: "Contact from Hudson-Zaußnig", // Subject line
      text: message + "\n" + email// html body
    }

    await new Promise((resolve, reject) => {
      transporter.sendMail(mailData, (err, info) => {
        if (err) {
          console.error(err);
          reject(err);
        } else {
          console.log(info);
          resolve(info);
        }
      })
    })
    
    // console.log(transporter);

    return new Response(
      JSON.stringify({ message: 'Message received successfully!' }),
      { status: 200 }
    );
  } catch (error) {
    return new Response(
      JSON.stringify({ message: 'Error processing your request.' }),
      { status: 500 }
    );
  }
};
