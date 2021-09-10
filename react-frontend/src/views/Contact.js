import React, {useState} from 'react'
import '../styles/app.scss'

export default function Contact() {

    const [name, setName] = useState("")
    const [company, setCompany] = useState("")
    const [email, setEmail] = useState("")
    const [phone, setPhone] = useState("")
    const [interestedIn, setInterestedIn] = useState("")
    const [message, setMessage] = useState("")

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
                            <input className="input-contact" onChange={(event) => setName(event.target.value)} type="text" placeholder="Name" name="name"/>
                            <input className="input-contact" onChange={(event) => setCompany(event.target.value)} type="text" placeholder="Company" name="company"/>
                        </div>
                        <div className="small-input-container-right">
                            <input className="input-contact" onChange={(event) => setEmail(event.target.value)} type="text" placeholder="Email" name="email"/>
                            <input className="input-contact" onChange={(event) => setPhone(event.target.value)} type="text" placeholder="Phone" name="phone"/>
                        </div>
                    </div>
                    <div className="large-input-container-full">
                        <input className="input-contact" onChange={(event) => setInterestedIn(event.target.value)} type="select" placeholder="Interested In" name="interest"/>
                        <textarea className="large-input-contact" onChange={(event) => setMessage(event.target.value)} placeholder="Message" name="message" rows="5" cols="50"/>

                    </div>
                    <div className="send-container">
                        <button className="send-button"></button>
                        <p>Send</p>
                    </div>

                </div>
            </div>
        </div>
    )
}
