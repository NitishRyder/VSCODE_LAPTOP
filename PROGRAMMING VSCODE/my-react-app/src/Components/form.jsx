import React from 'react';
import './form.css';

function moveto(){
  return(
    <div>
      Welcome
    </div>
  )
}

function Form() {
  return (
    <div className="form-container">
      <form className="form">
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" name="name" />

        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" />

        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" />
        <div className='button'>
          <button id='Login' onClick={moveto}>Login</button>
          <button id='Cancel'>Cancel</button>
        </div>
      </form>
    </div>
  );
}

export default Form;