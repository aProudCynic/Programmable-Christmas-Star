import React, { useState } from 'react';
import { SERVER_URL } from '../constants';

function IsOn() {

  const [isOn, setIsOn] = useState<boolean>(false);
  const [lastChecked, setLastChecked] = useState<Date | null>(null);

  const checkIsOn = async () => {
    const result = await fetch(`${SERVER_URL}/is_on`);
    if (result.ok) {
        const newIsOn = await result.json();
        console.log(newIsOn);
        setIsOn(newIsOn);
      }
  }

  return (
    <div>
      <p><input type="button" value="On?" onClick={checkIsOn} /> {isOn ? 'yes' : 'no' }</p>
      <p>last checked: {lastChecked ? lastChecked : 'never'}</p>
    </div>
  );
}

export default IsOn;
