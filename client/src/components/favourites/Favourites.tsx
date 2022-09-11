import React, { useContext, useEffect, useState } from 'react';
import { SERVER_URL } from '../../constants';
import IsOnContext from '../../store/started-context';
import { Colour } from '../../model/colour';

function Favourites() {

    const startedContext = useContext(IsOnContext);

    const initiatePurplePulse = async () => {
        const requestProperties: any = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                time_to_live: 1800,
                colour: new Colour('#FF00FF'),
                granularity: 100
            })
        }
        const result = await fetch(
            `${SERVER_URL}/start/radiate_colour`, requestProperties
        );
        if (result.ok) {
            startedContext.flipIsOn();
        }
    };

    return (
        <div className="Favourites">
            <h1>Favourites</h1>
            <input type="button" value="Purple pulse" onClick={initiatePurplePulse} disabled={startedContext.isOn} />
        </div>
    );
}

export default Favourites;
