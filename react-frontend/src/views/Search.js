import React, { useState } from 'react'
import axios from 'axios';
import JobCard from '../components/JobCard';

export default function Search() {

    const [jobTitle, setJobTitle] = useState("")
    const [location, setLocation] = useState("")
    const [jobResults, setJobResults] = useState([])
    
    const search = () => axios.post("http://localhost:5000/search", {job_title: jobTitle, location: location}).then((result) => setJobResults(result.data))

    return (
        <div className="job-finder">
            <div className="search-container">
                <input className="input-search" onChange={(event) => setJobTitle(event.target.value)} type="text" placeholder="Job Title" name="job_title"/>
                <input className="input-search" onChange={(event) => setLocation(event.target.value)} type="text" placeholder="Location" name="location"/>
                <button className="search-button" type="submit" value="Search" onClick={search}></button>
            </div>

            {jobResults.map((job) => 

            <div >
                <JobCard job={job} className="job-info"/>
            </div>
            )}
        </div>
    
    )
}