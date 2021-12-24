import React from 'react';
import { SERVER_URL } from '../constants';

const loopExplode = () => fetch(`${SERVER_URL}/loop/explode`, { method: 'POST'})

function Select() {
  return (
    <div className="Select">
      <input type="button" value="Loop explode" onClick={loopExplode}/>
    </div>
  );
}

export default Select;
