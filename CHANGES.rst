Changelog
=========

1.0.2 (????-??-??)
------------------

- `FromLayerSegments` class now outputs logging message if setting of new annotation indices fails, as error
  occurs before the `wai.annotations - Sourced ...` logging message, making it possible to track the image
  causing the problem.


1.0.1 (2022-05-11)
------------------

- Image segmentation annotations received `label_images` property with code from the ToLayerSegments conversion


1.0.0 (2021-05-20)
------------------

- Initial release after separation from wai.annotations main repo.
