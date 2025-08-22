export default class Building {
  constructor(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }

    if (new.target !== Building) {
      if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
        throw new Error('Class extending Building must override evacuationWarnignMessage');
      }
    }

    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
