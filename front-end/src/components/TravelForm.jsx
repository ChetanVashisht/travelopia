import React, { useState } from 'react'

export default function TravelForm() {
    const newForm = () => ({ name: '', email: '', destination: '', travellerCount: '', budget: '' })
    const [form, setForm] = useState(newForm)
    const handleChange = (e) => {
        const { value, name } = e.target
        setForm({ ...form, [name]: value})
    }
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(form)
        setForm(newForm)
    }
    return (
        <section>
            <h1>Travel Form</h1>
            <form>
                <span>Name</span><input onChange={handleChange} value={form.name} placeholder="Your Name" name="name" /><br />
                <span>Email</span><input onChange={handleChange} value={form.email} placeholder="joe@travelopia.com" name="email" /><br />
                <span>Where do you want to go?</span><select type="select" onChange={handleChange} value={form.destination} name="destination">
                    <option value='India'>India</option>
                    <option value='Africa'>Africa</option>
                    <option value='Europe'>Europe</option>
                </select><br />
                <span>Number of Travellers</span><input type="number" placeholder={4} onChange={handleChange} value={form.travellerCount} name="travellerCount" /><br />
                <span>Budget per person (in $)</span><input type="number" placeholder={100} onChange={handleChange} value={form.budget} name="budget" /><br />
                <button onClick={handleSubmit}> Submit </button>
            </form>
        </section>
    )
}
