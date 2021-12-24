import React, { useEffect, useState } from 'react';
import { SERVER_URL } from '../constants';

function Select() {

    const [lightProgrammes, setLightProgrammes] = useState([]);
    useEffect(() => {
        const request = fetch(`${SERVER_URL}/light_programmes`);
        request.then(
            result => result.json().then(
                fetchedLightProgrammes => {
                    setLightProgrammes(fetchedLightProgrammes)
                    setSelectedLightProgramme(fetchedLightProgrammes[0])
                }
            )
        )
    }, []);

    const [selectedLightProgramme, setSelectedLightProgramme] = useState(null);
    const handleChange = (event: any) => setSelectedLightProgramme(event.target.value);
    const loopLightProgramme = () => fetch(`${SERVER_URL}/loop/${selectedLightProgramme}`, { method: 'POST' });

    return (
        <div className="Select">
            <select name="cars" id="cars" onChange={handleChange}>
                {lightProgrammes.map(lightProgramme => <option value={lightProgramme}>{lightProgramme}</option>)}
            </select>
            <input type="button" value="Loop" onClick={loopLightProgramme} />
        </div>
    );
}

export default Select;
