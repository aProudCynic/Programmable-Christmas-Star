import React from 'react';

const SERVER_URL = 'http://smarthome.local:4000';
const stop = () => fetch(`${SERVER_URL}/stop`, { method: 'POST'})

function Stop() {
  return (
    <div className="Stop">
      <input type="button" value="Stop" onClick={stop}/>
    </div>
  );
}

export default Stop;
