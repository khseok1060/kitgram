import React from 'react';
import FacebookLogin from 'react-facebook-login';
import PropTypes from 'prop-types';
import formStyles from 'shared/formStyles.scss';

const SignupForm = (props, context) => (
  <div className={formStyles.formComponent}>
    <h3 className={formStyles.signupHeader}>
      {context.t("Sign up to see photos and videos from your friends")}.
    </h3>
    <FacebookLogin 
      appId="411884295948057"
      autoLoad={true}
      fields="name,eamil,picture"
      callback={props.handleFacebookLogin}
      cssClass={formStyles.facebookLink}
      icon={"fa-facebook-official"}
    />
    <span className={formStyles.divider}>{context.t("or")}</span>
    <form className={formStyles.form} onSubmit={props.handleSubmit}>
      <input 
        type="email" 
        placeholder={context.t("Email")} 
        className={formStyles.textInput}
        value={props.emailValue}
        name="email"
        onChange={props.handleInputChange}
      />
      <input 
        type="text" 
        placeholder={context.t("Full name")} 
        className={formStyles.textInput}
        value={props.fullNameValue}
        name="fullName"
        onChange={props.handleInputChange}
      />
      <input 
        type="text" 
        placeholder={context.t("Username")} 
        className={formStyles.textInput}
        value={props.usernameValue}
        name="username"
        onChange={props.handleInputChange}
      />
      <input 
        type="password" 
        placeholder={context.t("Password")} 
        className={formStyles.textInput}
        value={props.passwordValue}
        name="password"
        onChange={props.handleInputChange}
      />
      <input type="submit" value={context.t("Sign up")} className={formStyles.button}/>
    </form>
    <p className={formStyles.terms}>
      By Signing up, you agree to our <span>Terms & Privacy Policy</span>
    </p>
  </div>
);

SignupForm.propTypes = {
  emailValue: PropTypes.string.isRequired,
  fullNameValue: PropTypes.string.isRequired,
  usernameValue: PropTypes.string.isRequired,
  passwordValue: PropTypes.string.isRequired,
  handleInputChange: PropTypes.func.isRequired,
  handleSubmit: PropTypes.func.isRequired,
  handleFacebookLogin: PropTypes.func.isRequired
}

SignupForm.contextTypes = {
  t: PropTypes.func.isRequired
}

export default SignupForm;
