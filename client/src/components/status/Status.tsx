import React, { useContext, useState } from 'react';
import { SERVER_URL } from '../../constants';
import StatusContext from '../../store/status-context';
import Timer from '../timer/Timer';

function Status() {

  const statusContext = useContext(StatusContext);
  const [lastChecked, setLastChecked] = useState<Date | null>(null);

  const checkIsOn = async () => {
    const result = await fetch(`${SERVER_URL}/is_on`);
    if (result.ok) {
        const isOn = await result.json();
        console.log(isOn);
        isOn ? statusContext.setOn() : statusContext.setOff();
      }
  }

  return (
    <div>
      <p><input type="button" value="On?" onClick={checkIsOn} /> {startedContext.isOn ? 'yes' : 'no' }</p>
      <p>last checked: {lastChecked ? lastChecked : 'never'}</p>
      <p><Timer /></p>
    </div>
  );
}

export default Status;
