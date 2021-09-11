import React from 'react'
import '../styles/app.scss'

const deleteAccount = () => {}
const changePassword = () => {}

export default function Profile() {
            return (
                <div className="profile-page">
                    <div className="profile-container">
                        <div className="password-container">
                            <div className="header">Password Change: </div>
                            <input className="input-profile" type="text" placeholder="Current Password" name="current-password"/>
                            <input className="input-profile" type="text" placeholder="New Password" name="new-password"/>
                            <input className="input-profile" type="text" placeholder="Confirm New Password" name="confirm-password"/>
                            <button className="submit-button" type="submit" onClick={changePassword}></button>
                        </div>
                        <div className="delete-container">
                            <div className="header">Delete Account: </div>
                            <input className="input-profile" type="text" placeholder="Type 'DELETE'" name="check"/>
                            <button className="submit-button" type="submit" onClick={deleteAccount}></button>
                        </div>
                    </div>
                </div>

        )
    }
