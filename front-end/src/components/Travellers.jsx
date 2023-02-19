import React, { useState, useEffect } from 'react'
import Traveller from './Traveller'

export default function Travellers() {
    const [data, setData] = useState([])
    const renderTraveller = (traveller, i) => (<Traveller traveller={traveller} key={i} />)

    const loadTravellers = () => {
        fetch("http://localhost:8000/travellers")
            .then(resp => resp.json())
            .then(setData)
    }
    useEffect(loadTravellers, [])


    return (
        <section>
            <h1>List of Travellers</h1>
            <div className='rows'> {data.map(renderTraveller)}</div>
        </section>
    )
}
