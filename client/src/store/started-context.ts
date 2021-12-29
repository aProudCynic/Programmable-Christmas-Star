import React from 'react';

interface StartedContextProps {
  isStarted: boolean;
  flipStarted: Function;
}

const StartedContext = React.createContext<StartedContextProps>({isStarted: false, flipStarted: () => {}});

export default StartedContext;