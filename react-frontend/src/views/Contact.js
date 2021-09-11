import React, {useState} from 'react'
import '../styles/app.scss'
import axios from 'axios';

export default function Contact() {

    const [contactName, setContactName] = useState("")
    const [contactCompany, setContactCompany] = useState("")
    const [contactEmail, setContactEmail] = useState("")
    const [contactPhone, setContactPhone] = useState("")
    const [interestedIn, setInterestedIn] = useState("")
    const [contactMessage, setContactMessage] = useState("")
    const [contactResult, setContactResult] = useState([])

    axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    const contact = () => axios.post("http://localhost:5000/contact", {name: contactName, email: contactEmail, company: contactCompany, phone: contactPhone, interestedIn: interestedIn, message: contactMessage }).then((result) => setContactResult(result.data))

    return (
        <div className="contact-page">
            <div className="contact-container">
                <div className="info-container-left">
                    <h1>Get in touch!</h1>
                    <h2>I’ll do my best to get back to you as soon as possible.</h2>
                </div>
                <div className="input-container-right">
                    <div className="small-input-container-full">
                        <div className="small-input-container-left">
                            <input className="input-contact" onChange={(event) => setContactName(event.target.value)} type="text" placeholder="Name" name="name"/>
                            <input className="input-contact" onChange={(event) => setContactCompany(event.target.value)} type="text" placeholder="Company" name="company"/>
                        </div>
                        <div className="small-input-container-right">
                            <input className="input-contact" onChange={(event) => setContactEmail(event.target.value)} type="text" placeholder="Email" name="email"/>
                            <input className="input-contact" onChange={(event) => setContactPhone(event.target.value)} type="text" placeholder="Phone" name="phone"/>
                        </div>
                    </div>
                    <div className="large-input-container-full">
                        <input className="input-contact" onChange={(event) => setInterestedIn(event.target.value)} type="select" placeholder="Interested In" name="interest"/>
                        <textarea className="large-input-contact" onChange={(event) => setContactMessage(event.target.value)} placeholder="Message" name="message" rows="5" cols="50"/>

                    </div>
                    <div className="send-container">
                        <button className="send-button" onClick={contact}></button>
                        <p>Send</p>
                    </div>
                    <p className="message-sent-alert-success">
                    {contactResult['success']}</p>
                    <p className="message-sent-alert-fail">
                    {contactResult['error']}</p>
                    

                </div>
            </div>
        </div>
    )
}
