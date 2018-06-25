# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component


class Location(Component):
    """A Location component.
Update and track the current window.location object through the window.history state.
Use in conjunction with the `dash_core_components.Link` component to make apps with multiple pages.

Keyword arguments:
- id (string; required)
- pathname (string; optional): pathname in window.location - e.g., "/my/full/pathname"
- search (string; optional): search in window.location - e.g., "?myargument=1"
- hash (string; optional): hash in window.location - e.g., "#myhash"
- href (string; optional): href in window.location - e.g., "/my/full/pathname?myargument=1#myhash"
- refresh (boolean; optional): Refresh the page when the location is updated?

Available events: """
    def __init__(self, **kwargs):
        self._prop_names = ['id', 'pathname', 'search', 'hash', 'href', 'refresh']
        self._type = 'Location'
        self._namespace = 'dash_core_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'pathname', 'search', 'hash', 'href', 'refresh']
        self.available_wildcard_properties =            []

        for k in ['id']:
            if k not in kwargs:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Location, self).__init__(**kwargs)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Location(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Location(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')