import React from "react";
import PropTypes from "prop-types";
import styles from "./styles.scss";

const CommentsBox = (props, context) => (
  <form>
    <textarea placeholder={context.t("Add a comment...")} />
  </form>
)

CommentsBox.contextTypes = {
  t: PropTypes.func.isRequired
}

export default CommentsBox;
