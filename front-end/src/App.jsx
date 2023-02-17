import React from 'react'
import { Link, Routes, Route } from 'react-router-dom'
import TravelForm from './components/TravelForm'
import Travellers from './components/Travellers'

function App() {
    return (
        <div>
            <nav>
                <Link to="/">Travel</Link>
                <Link to="/travellers">Travellers</Link>
            </nav>
            <Routes>
                <Route exact path="/" element={<TravelForm />} />
                <Route exact path="/travellers" element={<Travellers />} />
            </Routes>
        </div>
    )
}

export default App
