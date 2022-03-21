import React, { useContext, useState } from 'react';
import { SERVER_URL } from '../../constants';
import IsOnContext from '../../store/started-context';

function IsOn() {

  const startedContext = useContext(IsOnContext);
  const [lastChecked, setLastChecked] = useState<Date | null>(null);

  const checkIsOn = async () => {
    const result = await fetch(`${SERVER_URL}/is_on`);
    if (result.ok) {
        const isOn = await result.json();
        console.log(isOn);
        isOn ? startedContext.setOn() : startedContext.setOff();
      }
  }

  return (
    <div>
      <p><input type="button" value="On?" onClick={checkIsOn} /> {startedContext.isOn ? 'yes' : 'no' }</p>
      <p>last checked: {lastChecked ? lastChecked : 'never'}</p>
    </div>
  );
}

export default IsOn;
