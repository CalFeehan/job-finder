import React from 'react'

export default function JobCard({job}) {

    return (
        <div>
            <div class="job-card">
                <strong> { job['title'] } </strong><br/>
                Company: { job['company'] } <br/>
                Location: { job['location'] } <br/>
                Salary: { job['salary'] } <br/>
                Summary: { job['summary'] } <br/>
                <br/>
            </div>
            <div class="save-container">
                <form>
                    <br/>
                    <br/>
                    <br/>
                    <input type="submit" value="SAVE" class="save-button"/> <br/>
                    <br/>
                    <br/>
                </form>
            </div>
        </div>
    )
}

/*
        

*/
