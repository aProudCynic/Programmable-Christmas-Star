import React, { useContext, useEffect, useState } from 'react';
import { SERVER_URL } from '../constants';
import StartedContext from '../store/started-context';

interface LightProgramme {
    name: string;
    parameters: string[];
}

function Select() {

    const startedContext = useContext(StartedContext);

    const [lightProgrammes, setLightProgrammes] = useState<LightProgramme[]>([]);    
    useEffect(() => {
        const request = fetch(`${SERVER_URL}/light_programmes`);
        request.then(
            result => result.json().then(
                fetchedLightProgrammes => {
                    fetchedLightProgrammes.forEach((element: any[]) => {
                        console.log(element)
                    });
                    setLightProgrammes(fetchedLightProgrammes)
                    setSelectedLightProgramme(fetchedLightProgrammes[0])
                }
            )
        )
    }, []);

    const [selectedLightProgramme, setSelectedLightProgramme] = useState<LightProgramme | undefined>(undefined);
    const handleChange = (event: any) => setSelectedLightProgramme(lightProgrammes.find(lightProgramme => lightProgramme.name === event.target.value));
    
    const loopLightProgramme = async () => {
        if (selectedLightProgramme) {
            const result = await fetch(`${SERVER_URL}/loop/${selectedLightProgramme.name}`, { method: 'POST' });
            if (result.ok) {
                startedContext.flipStarted();
            }
        }
    };

    return (
        <div className="Select">
            <select name="ligthProgramme" id="ligthProgramme" onChange={handleChange} disabled={startedContext.isStarted}>
                {lightProgrammes.map(lightProgramme => <option value={lightProgramme.name}>{lightProgramme.name}</option>)}
            </select>
            { selectedLightProgramme && selectedLightProgramme.parameters ? selectedLightProgramme.parameters.map(
                parameter => <p><label htmlFor={parameter}>{parameter}</label> <input type="text" id={parameter} name={parameter} defaultValue="0"></input></p>
            ) : null }
            <input type="button" value="Loop" onClick={loopLightProgramme} disabled={startedContext.isStarted}/>
        </div>
    );
}

export default Select;
