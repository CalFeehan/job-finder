import React from 'react'
import '../styles/app.scss'

export default function Dashboard(props) {
    console.log(props)
    return (
        <div class="dashboard">
            <section>
                <form method='GET'> 
                    <button type="submit" class='job-finder-button'>Job Finder</button>
                </form>
            </section>
            <section>
                <form method='GET'> 
                    <button type="submit" class='application-tracker-button'>Application Tracker</button>
                </form>
            </section>
        </div>
    )
}