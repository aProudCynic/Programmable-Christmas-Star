import React, { useState } from 'react';
import './App.css';
import Select from './select/Select';
import Stop from './stop/Stop';
import StartedContext from './store/started-context';

function App() {

  const [started, setStarted] = useState(false);
  
  return (
    <div className="App">
      <StartedContext.Provider value={{isStarted: started, flipStarted: () => setStarted(!started)}}>
        <Stop></Stop>
        <Select></Select>
      </StartedContext.Provider>
    </div>
  );
}

export default App;
