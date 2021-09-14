import React, {useState} from 'react'
import axios from 'axios';

export default function JobCard({job}) {

    const changeSaveButton = () => {document.querySelector(".save-button").innerText = jobSaved[0];}

    const [title, setTitle] = useState("")
    const [company, setCompany] = useState("")
    const [location, setLocation] = useState("")
    const [salary, setSalary] = useState("")
    const [summary, setSummary] = useState("")
    const [jobSaved, setJobSaved] = useState([])

    axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
    const save = () => {
        setTitle(job['title']);
        setCompany(job['company']);
        setLocation(job['location']);
        setSalary(job['salary']);
        setSummary(job['summary']);
        
        axios.post("http://localhost:5000/save-job", {title: title, company: company, location: location, salary: salary, summary: summary}).then((result) => {setJobSaved(result.data)});
        //changeSaveButton();    
    }

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
                <button className="save-button" onClick={save}>Save</button>
            </div>
        </div>
    )
}

/*
        

*/
