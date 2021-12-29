import React, { useContext, useEffect, useState } from 'react';
import { SERVER_URL } from '../constants';
import StartedContext from '../store/started-context';

function Select() {

    const startedContext = useContext(StartedContext);

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
    const loopLightProgramme = async () => {
        const result = await fetch(`${SERVER_URL}/loop/${selectedLightProgramme}`, { method: 'POST' });
        if (result.ok) {
            startedContext.flipStarted();
        }
    };

    return (
        <div className="Select">
            <select name="cars" id="cars" onChange={handleChange} disabled={startedContext.isStarted}>
                {lightProgrammes.map(lightProgramme => <option value={lightProgramme}>{lightProgramme}</option>)}
            </select>
            <input type="button" value="Loop" onClick={loopLightProgramme} disabled={startedContext.isStarted}/>
        </div>
    );
}

export default Select;
