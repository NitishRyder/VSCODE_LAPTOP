import React, { useState } from 'react';
import './form.css';


function ClickMe(){
  alert("You clicked me!")
}

function Form() {
  function handleSubmit(e){
    e.preventDefault();
    console.log('You Clicked Submit.')
  }
  return (
    <div className="form-container">
      <form className="form">
        <label htmlFor="name">Name:</label>
        <input type="text" id="name" name="name" />

        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" />

        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" />
        <div className='button' onSubmit={handleSubmit}>
          <div className='Login'>Login</div>
          <div className='Cancel'>Cancel</div>
        </div>
        
      </form>
    </div>
  );
}

export default Form;