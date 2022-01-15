import React, { useContext, useEffect, useState } from 'react';
import { SERVER_URL } from '../constants';
import StartedContext from '../store/started-context';

class Colour {
    red: number;
    green: number;
    blue: number;

    constructor(hexCode?: string) {
        if (!hexCode) {
            this.red = 0;
            this.green = 0;
            this.blue = 0;
        } else {
            if (!hexCode.match(/#[a-f0-9]{6}/)) {
                throw new Error(`Hex code is invalid: ${hexCode}`)
            }
            this.red = parseInt(hexCode.slice(1, 3), 16);
            this.green = parseInt(hexCode.slice(3, 5), 16);
            this.blue = parseInt(hexCode.slice(5, 7), 16);
        }
    }
}

interface LightProgramme {
    name: string;
    parameters: ParameterDescriptor[];
}

interface ParameterDescriptor {
    name: string;
    type: string;
}

function Select() {

    const startedContext = useContext(StartedContext);

    const [lightProgrammes, setLightProgrammes] = useState<LightProgramme[]>([]);
    const [selectedLightProgramme, setSelectedLightProgramme] = useState<LightProgramme | undefined>(undefined);
    const [parameters, setParameters] = useState<Record<string, string | number | Colour> | undefined>(undefined);

    useEffect(() => {
        const request = fetch(`${SERVER_URL}/light_programmes`);
        request.then(
            result => result.json().then(
                fetchedLightProgrammes => {
                    fetchedLightProgrammes.forEach((element: any[]) => {
                        console.log(element)
                    });
                    setLightProgrammes(fetchedLightProgrammes);
                    const selectedProgramme = fetchedLightProgrammes[0];
                    setSelectedLightProgramme(selectedProgramme);
                    resetParametersByDefaultsFor(selectedProgramme.parameters);
                }
            )
        )
    }, []);

    const getDefaultValueFor = (type: string) => {
        switch (type) {
            case 'str':
                return '';
            case 'int':
                return 0;
            case 'Colour':
                return new Colour('#000000');
        }
    }

    const handleChange = (event: any) => {
        const selectedProgramme = lightProgrammes.find(lightProgramme => lightProgramme.name === event.target.value);
        setSelectedLightProgramme(selectedProgramme);
        if (selectedProgramme) {
            resetParametersByDefaultsFor(selectedProgramme);
        };
    }

    const loopLightProgramme = async () => {
        if (selectedLightProgramme) {
            const result = await fetch(`${SERVER_URL}/loop/${selectedLightProgramme.name}`, { method: 'POST' });
            if (result.ok) {
                startedContext.flipStarted();
            }
        }
    };

    const handleColorParameterChange = (event: any) => {
        const newColour = new Colour(event.target.value);
        const parameterName = event.target.name;
        const newParameters = { ...parameters };
        newParameters[parameterName] = newColour;
        setParameters(newParameters);
    }

    function resetParametersByDefaultsFor(programme: LightProgramme) {
        const newParameters: any = {};
        programme.parameters.forEach(
            (parameterDescriptor: ParameterDescriptor) => newParameters[parameterDescriptor.name] = getDefaultValueFor(parameterDescriptor.type)
        );
        setParameters(newParameters);
    }

    const mapParameterDescriptorToHtmlElement = (parameter: ParameterDescriptor) => {
        switch (parameter.type) {
            case 'str':
                return <p><label htmlFor={parameter.name}>{parameter.name}</label> <input type="text" id={parameter.name} name={parameter.name}></input></p>
            case 'Colour':
                return <p><label htmlFor={parameter.name}>{parameter.name}</label> <input type="color" id={parameter.name} name={parameter.name} onChange={handleColorParameterChange}></input></p>
        }
    }

    return (
        <div className="Select">
            <select name="ligthProgramme" id="ligthProgramme" onChange={handleChange} disabled={startedContext.isStarted}>
                {lightProgrammes.map(lightProgramme => <option value={lightProgramme.name}>{lightProgramme.name}</option>)}
            </select>
            {selectedLightProgramme && selectedLightProgramme.parameters ? selectedLightProgramme.parameters.map(
                parameter => mapParameterDescriptorToHtmlElement(parameter)
            ) : null}
            <input type="button" value="Loop" onClick={loopLightProgramme} disabled={startedContext.isStarted} />
        </div>
    );
}

export default Select;
