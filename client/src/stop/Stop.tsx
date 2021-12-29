import React, { useContext } from 'react';
import { SERVER_URL } from '../constants';
import StartedContext from '../store/started-context';

function Stop() {

  const startedContext = useContext(StartedContext);

  const stop = async () => {
    const result = await fetch(`${SERVER_URL}/stop`, { method: 'POST' })
    if (result.ok) {
      startedContext.flipStarted();
    }
  }

  return (
    <div className="Stop">
      <input type="button" value="Stop" onClick={stop} disabled={!startedContext.isStarted} />
    </div>
  );
}

export default Stop;
