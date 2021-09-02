import React from 'react'
import '../styles/app.scss'

export default function Dashboard(props) {
    console.log(props)
    return (
        <div className="dashboard">
            <section>
                <button onClick={()=>props.history.push('/search')} className='job-finder-button'>Job Finder</button>
            </section>
            <section>
                <button onClick={()=>props.history.push('/applications')} className='application-tracker-button'>Application Tracker</button>
            </section>
        </div>
    )
}