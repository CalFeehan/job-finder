import axios from 'axios';
import React, {useState} from 'react'

export default function Applications() {

    const [savedJobs, setSavedJobs] = useState([])

    const getJobs = () => axios.get("http://localhost:5000/get-jobs").then((result) => setSavedJobs(result.data))

    return (
        <div>
            {<button onClick={getJobs}>BUTTON</button>}
            <div>{savedJobs}</div>
        </div>
    )
}
