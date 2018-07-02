import React from 'react';
import PropTypes from 'prop-types';
import { Route, Switch } from "react-router-dom";
import './styles.scss';
import Footer from 'components/Footer';
import Auth from 'components/Auth';
import Navigation from 'components/Navigation';
import Feed from 'components/Feed';
import Explore from 'components/Explore';

const App  = props => [
  // Nav,
  props.isLoggedIn ? <Navigation key={1} /> : null, 
  // Route,
  props.isLoggedIn ? <PrivateRoutes key={2} /> : <PublicRoutes key={2} />,
  // Footer
  <Footer key={3} />
];

App.propTypes = {
  isLoggedIn: PropTypes.bool.isRequired
}

const PrivateRoutes = props => (
  <Switch>
    <Route key="1" exact path="/" component={Feed} />,
    <Route key="2" exact path="/explore" component={Explore} />
    <Route path="/search/:serachTerm" render={() => "search"} />
  </Switch>
);

const PublicRoutes = props => (
  <Switch>
    <Route exact path="/" component={Auth} />,
    <Route exact path="/recover" render={() => "password"} />
  </Switch>
);

export default App;
