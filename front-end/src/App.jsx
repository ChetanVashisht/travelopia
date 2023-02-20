import React from 'react'
import { Link, Routes, Route, useLocation } from 'react-router-dom'
import TravelForm from './components/TravelForm'
import Travellers from './components/Travellers'

function App() {
    const getActive = (loc) => useLocation().pathname == loc ? 'active' : '';
    return (
        <div>
            <nav>
                <Link to="/" className={`navitem ${getActive('/')}`}>Travel</Link>
                <Link to="/tourists" className={`navitem ${getActive('/tourists')}`}>Travellers</Link>
            </nav>
            <Routes>
                <Route exact path="/" element={<TravelForm />} />
                <Route exact path="/tourists" element={<Travellers />} />
            </Routes>
        </div>
    )
}

export default App
