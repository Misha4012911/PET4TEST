import React from 'react';
import UserList from './components/UserList'; // Импортируем компонент

const App = () => {
  return (
    <div>
      <h1>My App</h1>
      <UserList /> {/* Вызываем компонент */}
    </div>
  );
}

export default App;