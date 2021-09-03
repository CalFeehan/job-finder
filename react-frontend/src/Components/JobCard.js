import React from 'react'

export default function JobCard({job}) {

    return (
        <div className="job-container">
            <div className="job-card">
                <strong> { job['title'] } </strong><br/>
                Company: { job['company'] } <br/>
                Location: { job['location'] } <br/>
                Salary: { job['salary'] } <br/>
                Summary: { job['summary'] } <br/>
            </div>
            <div className="save-container">
                <button className="save-button">Save</button>
            </div>
        </div>
    )
}

/*
        

*/
