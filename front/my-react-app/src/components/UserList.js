import React, { useState, useEffect } from 'react';
import apiUrl from './config';

const UserList = () => {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(apiUrl + '/names'); // использование конкатенации строк для формирования URL
        const data = await response.json();
        setUserData(data.users);
      } catch (error) {
        console.error('Error fetching data', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>User Data:</h1>
      {userData ? (
        <ul>
          {userData.map((user) => (
            <li key={user.id}>Name: {user.name}, Login: {user.login}</li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default UserList;