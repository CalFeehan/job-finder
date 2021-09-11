import React from 'react'
import '../styles/app.scss'

export default function Dashboard(props) {
    console.log(props)
    return (
        <div className="dashboard">
            <button className="job-finder-button" onClick={()=>props.history.push('/search')}>
                <div className='job-finder-text'>
                    Job Finder
                </div>
                <div className="dashboard-logos" />
            </button>
            <button className="application-tracker-button" onClick={()=>props.history.push('/applications')}>
                <div className='application-tracker-text'>
                    Application Tracker
                </div>
                <div className="dashboard-logos" />
            </button>
        </div>
    )
}