import React, { useContext } from 'react';
import { SERVER_URL } from '../../constants';
import StatusContext from '../../store/status-context';

function Stop() {

  const startedContext = useContext(StatusContext);

  const stop = async () => {
    const result = await fetch(`${SERVER_URL}/stop`, { method: 'POST' })
    if (result.ok) {
      startedContext.flipIsOn();
    }
  }

  return (
    <div className="Stop">
      <input type="button" value="Stop" onClick={stop} disabled={!startedContext.isOn} />
    </div>
  );
}

export default Stop;
