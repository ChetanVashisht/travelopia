import React from 'react'

export default function Traveller({ traveller }) {
    return (
        <div className="details">
            <summary><b>{traveller.name}</b></summary>
            <label>Email: </label> <span>{traveller.email}</span> <br />
            <label>Destination: </label> <span>{traveller.destination}</span> <br />
            <label>No Of Travellers: </label> <span>{traveller.travellerCount}</span> <br />
            <label>Budget: </label> <span>{traveller.budget}</span> <label>$/person</label> <br />
        </div>
    )
}
