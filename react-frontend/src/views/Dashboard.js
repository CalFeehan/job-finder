import React from 'react'
import '../styles/app.scss'

export default function Dashboard(props) {
    console.log(props)
    return (
        <div className="dashboard">
            <div className="job-finder-container">
                <button onClick={()=>props.history.push('/search')} className='job-finder-button'>Job Finder</button>
            </div>
            <div className="application-tracker-container">
                <button onClick={()=>props.history.push('/applications')} className='application-tracker-button'>Application Tracker</button>
            </div>
        </div>
    )
}