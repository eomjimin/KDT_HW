import express from 'express'
import * as database from'./database.js'
import { body } from 'express-validator'

const router = express.Router()

router.get('/', database.getStoreInformation)

export default router