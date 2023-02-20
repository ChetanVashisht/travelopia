import React, { useState, useEffect, useRef } from 'react'

export default function TravelForm() {
    const newForm = () => ({ name: '', email: '', destination: '', travellerCount: '', budget: '' })
    const [form, setForm] = useState(newForm)
    const [isValidForm, setIsValidForm] = useState(false)
    const emailField = useRef(null)

    const handleChange = (e) => {
        const { value, name } = e.target
        setForm({ ...form, [name]: value })
    }

    const isValidName = (name) =>  String(name).length > 2
    const isValidEmail = () => emailField.current.checkValidity()
    const isValidDestination = (destination) => ['Africa', 'India', 'Europe'].includes(destination)
    const isValidTravellerCount = (tc) => parseInt(tc) > 0
    const isValidBudget = (budget) => parseFloat(budget) > 0

    const isValid = () => {
        return isValidEmail(form.email) && isValidBudget(form.budget) && isValidTravellerCount(form.travellerCount) && isValidDestination(form.destination) && isValidName(form.name)
    }

    useEffect(() => setIsValidForm(isValid), [form])

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(form)
        fetch('http://localhost:8000/travellers/', { method: 'post', body: JSON.stringify(form), headers: { 'content-type': 'application/json'} })
            .then(resp => console.log(resp.json))
        // setForm(newForm)
    }
    return (
        <section>
            <h1>Travel Form</h1>
            <form>
                <span>Name</span><input onChange={handleChange} value={form.name} placeholder="Your Name" name="name" /><br />
                <span>Email</span><input onChange={handleChange} value={form.email} ref={emailField} placeholder="joe@travelopia.com" name="email" /><br />
                <span>Where do you want to go?</span><select type="select" onChange={handleChange} value={form.destination} name="destination">
                    <option value='' disabled>-- Choose Destination --</option>
                    <option value='India'>India</option>
                    <option value='Africa'>Africa</option>
                    <option value='Europe'>Europe</option>
                </select><br />
                <span>Number of Travellers</span><input type="number" placeholder={4} onChange={handleChange} value={form.travellerCount} name="travellerCount" /><br />
                <span>Budget per person (in $)</span><input type="number" placeholder={100} onChange={handleChange} value={form.budget} name="budget" /><br />
                <button onClick={handleSubmit} disabled={!isValidForm}> Submit </button>
            </form>
        </section>
    )
}
