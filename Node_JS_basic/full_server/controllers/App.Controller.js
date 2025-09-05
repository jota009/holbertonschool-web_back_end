// full_server/controllers/AppController.js
export default class AppController {
  static getHomepage(req, res) {
    res.status(200).type('text').send('Hello Holberton School!');
  }
}
