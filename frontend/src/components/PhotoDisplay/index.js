import React from "react";
import PropTypes from "prop-types";
import Ionicons from "react-ionicons";
import styles from "./styles.scss";

const PhotoDisplay = props => (
  <div className={styles.column}>
    <img src={props.photo.file} className={styles.photo} alt={props.photo.id}/>
    <div className={styles.overlay}>
      <span className={styles.data}>
        <Ionicons icon="ios-heart" fontSize="22px" color="white" />{" "}
        {props.photo.like_count}
      </span>
      <span className={styles.data}>
        <Ionicons icon="ios-text" fontSize="22px" color="white" />{" "}
        {props.photo.comment_count}
      </span>
    </div>
  </div>
)

PhotoDisplay.propTypes = {
  photo: PropTypes.shape({
    file: PropTypes.string.isRequired,
    comment_count: PropTypes.number.isRequired,
    like_count: PropTypes.number.isRequired
  }).isRequired
};

export default PhotoDisplay;
