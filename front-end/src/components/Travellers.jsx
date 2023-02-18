import React, { useState, useEffect } from 'react'
import sampleData from '../assets/sampleData'
import Traveller from './Traveller'

export default function Travellers() {
    const [data, setData] = useState([])

    const apiCall = () => setData(sampleData)
    const renderTraveller = (traveller, i) => (<Traveller traveller={traveller} key={i} />)
    useEffect(apiCall, [])
    return (
        <section>
            <h1>List of Travellers</h1>
            <div className='rows'> {data.map(renderTraveller)}</div>
        </section>
    )
}
